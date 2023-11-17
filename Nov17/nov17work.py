# creating a net profit function

def Netprofit(quantity, price, cost):
    print((price - cost) * quantity )
    return (price - cost) * quantity  

if __name__=="__main__":
    Netprofit(50,100,20)


import  os

class assignment_handler:
     
    def __init__(self):
        self.path_to_assignments = 'C:\Users\MCOB PHD 17\Desktop\BA798\assignments'
        self.list_of_files = self._get_assignment()

    def _get_assignment(self):
        assisgnment = os.listdir(self.path_to_assignments)
        return assignments
    
        def print_assignment_path(self):
        files = os.listdir(self.path_to_files)
        return files
        


    def grab_assignmnt_dict(self, num, formatted=True):
        assignment_dict = {}
        for assignment in self.list_of_assignments[:num]:
            asign_path = self


