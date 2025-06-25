class Increment:
    def __iter__(self):
        self.x=1
        return self
    def __next__(self):
        if self.x < 11:
          n=self.x
          self.x+=1
          return n
        else:
            raise StopIteration
in_obj=Increment()
itrs_obj=iter(in_obj)
for i in itrs_obj:
    print(i)