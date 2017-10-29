# class binarysearch extending list class 
class binarySearch(list):
    def __init__(self, the_max, step):
        self.step=step
        self.the_max=the_max
        if the_max in self.toTwenty():
            self.extend(self.toTwenty())
        elif the_max in self.toForty():
            self.extend(self.toForty())
        elif the_max in self.ten_to_thousand():
            self.extend(self.ten_to_thousand())

        self.length = len(self)

    def toTwenty(self):
        return range(self.step,(self.the_max * self.step)+1,self.step)
    def toForty(self):
        return range(self.step,(self.the_max * self.step)+1,self.step)
    def ten_to_thousand(self):
        return range(self.step,(self.the_max * self.step)+1,self.step)
   
    def search(self, number):
        first = 0
        last = self.length-1
        found = False
        index = 0
        counter = 0

        if number == self[first]:
            index = first
            found = True
        elif number == self[last]:
            index = last
            found = True
        elif number not in self:
            found = True
            index = -1

        while first<=last and not found:
            midpoint = (first + last)//2 #split to half
            # if number is equal to our middle term we return true
            if self[midpoint] == number: 
                found = True
                index = midpoint
            # else repeat again
            else:
                counter += 1
                if number < self[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return {'count': counter, 'index': index}