class C2dvec:
    def_init_(self,i,j):
    self.icap = i
    self.jcap = j
    def _str _(self):
   returnf"{self.icap}"+{self.jcap}
    
class Cdvec(C2dvec):
    def_int_(self,i,j,k):
#  self.icap = i
#  self.jcap = j
super()._init_(i,j))
 self.kcap = k
 
 def_str_(self):
     return f"(self.icap)"+(self.jcap)+ (self.kcap)
 
 v2d = C2dVec(1,3)
 v3d = C2dvec(1,9,7)
 print(v2d)
 print(v3d)
