x0 = 3; v0 =2; t0 = 0;
tf = 1.5;
h = .2;
#--------------------------------------------------------
T = function(IC){
    x = IC[1];
    v = IC[2];
    t = IC[3];
    c(v, -6*x - t*v, 1);
};
#-------------------------------------------------------
# Don’t change anything below here unless you know what
# you are doing!   :-)
#-------------------------------------------------------
EulerTangentMethod = function(IC,tf,h,T){  # Euler Method Function Start
  En = IC;
  Tn = T(En);
  n = 0;
  xn = En[1];  vn = En[2];  tn = En[3];
  Txn = Tn[1]; Tvn = Tn[2]; Ttn = Tn[3];
  NumOfSteps = abs(tf-tn)/h; NumOfSteps;
  h = h*(tf - tn)/abs(tf-tn);
  for (k in 1:NumOfSteps){
      EnPlus1 = En + h*Tn;
      En = EnPlus1;
      Tn = T(En);
      n[k+1] = k;
      xn[k+1] =  En[1]; vn[k+1] = En[2]; tn[k+1] = En[3];
      Txn[k+1] = Tn[1]; Tvn[k+1] = Tn[2]; Ttn[k+1] = Tn[3];
  };                          # for loop end
  out =   cbind(n,xn,vn,tn,Txn,Tvn);  # output
}                                   # end of function
#---------------------------------------------
IC = c(x0,v0,t0);
a = EulerTangentMethod(IC,tf,h,T); # Store output in a
plot(a[,4],a[,2],  lwd = 2,
xlab = "t", ylab = "x");
grid();
a[,1:4];
