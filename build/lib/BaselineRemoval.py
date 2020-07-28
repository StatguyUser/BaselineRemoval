import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.sparse import csc_matrix, eye, diags
from scipy.sparse.linalg import spsolve
import warnings
warnings.filterwarnings('ignore')

class BaselineRemoval():
    '''input_array: A pandas dataframe column provided in input as dataframe['input_df_column']. It can also be a Python list object
    degree: Polynomial degree
    '''     
    def __init__(self,input_array):
        self.input_array=input_array
        self.lin=LinearRegression()

    def poly(self,input_array_for_poly,degree_for_poly):
        '''qr factorization of a matrix. q` is orthonormal and `r` is upper-triangular.
        - QR decomposition is equivalent to Gram Schmidt orthogonalization, which builds a sequence of orthogonal polynomials that approximate your function with minimal least-squares error
        - in the next step, discard the first column from above matrix.

        - for each value in the range of polynomial, starting from index 0 of pollynomial range, (for k in range(p+1))
            create an array in such a way that elements of array are (original_individual_value)^polynomial_index (x**k)
        - concatenate all of these arrays created through loop, as a master array. This is done through (np.vstack)
        - transpose the master array, so that its more like a tabular form(np.transpose)'''
        input_array_for_poly = np.array(input_array_for_poly)
        X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1))))
        return np.linalg.qr(X)[0][:,1:]
    def ModPoly(self,degree=2,repitition=100,gradient=0.001):
        '''Implementation of Modified polyfit method from paper: Automated Method for Subtraction of Fluorescence from Biological Raman Spectra, by Lieber & Mahadevan-Jansen (2003)
        
        degree: Polynomial degree, default is 2
        repitition: How many iterations to run. Default is 100
        gradient: Gradient for polynomial loss, default is 0.001. It measures incremental gain over each iteration. If gain in any iteration is less than this, further improvement will stop
        '''

        #initial improvement criteria is set as positive infinity, to be replaced later on with actual value
        criteria=np.inf

        baseline=[]
        corrected=[]

        ywork=self.input_array
        yold=self.input_array
        yorig=self.input_array

        polx=self.poly(list(range(1,len(yorig)+1)),degree)
        nrep=0

        while (criteria>=gradient) and (nrep<=repitition):
            ypred=self.lin.fit(polx,yold).predict(polx)
            ywork=np.array(np.minimum(yorig,ypred))
            criteria=sum(np.abs((ywork-yold)/yold))
            yold=ywork
            nrep+=1
        corrected=yorig-ypred
        corrected=np.array(list(corrected))
        return corrected
    
    def IModPoly(self,degree=2,repitition=100,gradient=0.001):
        '''IModPoly from paper: Automated Autofluorescence Background Subtraction Algorithm for Biomedical Raman Spectroscopy, by Zhao, Jianhua, Lui, Harvey, McLean, David I., Zeng, Haishan (2007)

        degree: Polynomial degree, default is 2        
        repitition: How many iterations to run. Default is 100
        gradient: Gradient for polynomial loss, default is 0.001. It measures incremental gain over each iteration. If gain in any iteration is less than this, further improvement will stop
        '''

        yold=np.array(self.input_array)
        yorig=np.array(self.input_array)
        corrected=[]

        nrep=1
        ngradient=1

        polx=self.poly(list(range(1,len(yorig)+1)),degree)
        ypred=self.lin.fit(polx,yold).predict(polx)
        Previous_Dev=np.std(yorig-ypred)

        #iteration1
        yold=yold[yorig<=(ypred+Previous_Dev)]
        polx_updated=polx[yorig<=(ypred+Previous_Dev)]
        ypred=ypred[yorig<=(ypred+Previous_Dev)]

        for i in range(2,repitition+1):
            if i>2:
                Previous_Dev=DEV
            ypred=self.lin.fit(polx_updated,yold).predict(polx_updated)
            DEV=np.std(yold-ypred)

            if np.abs((DEV-Previous_Dev)/DEV) < gradient:
                break
            else:
                for i in range(len(yold)):
                    if yold[i]>=ypred[i]+DEV:
                        yold[i]=ypred[i]+DEV
        baseline=self.lin.predict(polx)
        corrected=yorig-baseline
        return corrected

    def _WhittakerSmooth(self,x,w,lambda_,differences=1):
        '''
        Penalized least squares algorithm for background fitting

        input
            x: input data (i.e. chromatogram of spectrum)
            w: binary masks (value of the mask is zero if a point belongs to peaks and one otherwise)
            lambda_: parameter that can be adjusted by user. The larger lambda is,  the smoother the resulting background
            differences: integer indicating the order of the difference of penalties

        output
            the fitted background vector
        '''
        X=np.matrix(x)
        m=X.size
        i=np.arange(0,m)
        E=eye(m,format='csc')
        D=E[1:]-E[:-1] # numpy.diff() does not work with sparse matrix. This is a workaround.
        W=diags(w,0,shape=(m,m))
        A=csc_matrix(W+(lambda_*D.T*D))
        B=csc_matrix(W*X.T)
        background=spsolve(A,B)
        return np.array(background)

    def ZhangFit(self,lambda_=100, porder=1, itermax=15):
        '''
        Implementation of Zhang fit for Adaptive iteratively reweighted penalized least squares for baseline fitting. Modified from Original implementation by Professor Zhimin Zhang at https://github.com/zmzhang/airPLS/
        
        lambda_: parameter that can be adjusted by user. The larger lambda is,  the smoother the resulting background, z
        porder: adaptive iteratively reweighted penalized least squares for baseline fitting
        '''

        yorig=np.array(self.input_array)
        corrected=[]

        m=yorig.shape[0]
        w=np.ones(m)
        for i in range(1,itermax+1):
            corrected=self._WhittakerSmooth(yorig,w,lambda_, porder)
            d=yorig-corrected
            dssn=np.abs(d[d<0].sum())
            if(dssn<0.001*(abs(yorig)).sum() or i==itermax):
                if(i==itermax): print('WARING max iteration reached!')
                break
            w[d>=0]=0 # d>0 means that this point is part of a peak, so its weight is set to 0 in order to ignore it
            w[d<0]=np.exp(i*np.abs(d[d<0])/dssn)
            w[0]=np.exp(i*(d[d<0]).max()/dssn) 
            w[-1]=w[0]
        return yorig-corrected

if __name__=="__main__":
        input_array = np.random.randint(0, 10, 20)
        obj = BaselineRemoval(input_array)
        Modpoly_output=obj.ModPoly(2)
        Imodpoly_output=obj.IModPoly(2)
        Zhangfit_output=obj.ZhangFit()
        print('Original input:',input_array)
        print('Modpoly base corrected values:',Modpoly_output)
        print('Imodpoly base corrected values:',Imodpoly_output)
        print('ZhangFit base corrected values:',Zhangfit_output)
