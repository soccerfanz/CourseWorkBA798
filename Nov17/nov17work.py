import os

class assignment_handler:
    
    def __init__(self):
        """This class is used to handle the assignments. It has a method to print the assignments, and a method to return a dictionary of the assignments."""
        self.path_to_assignments = 'C:\\Users\\MCOB PHD 17\\Desktop\\BA798\\assignments\\'
        self.list_of_assignments = self._get_assignments()

    def _get_assignments(self):
        """This method returns a list of the assignments."""
        assignments = os.listdir(self.path_to_assignments)
        return assignments
    
    def print_assignment_paths(self):
        """This method prints the paths to the assignments."""
        assignments_list_path = self._get_assignments()
        for assignment in assignments_list_path:
            print(assignment)

    def grab_assignments_dict(self, num, formatted=True):
        """This method returns a dictionary of the assignments. The keys are the assignment names, and the values are the assignment contents."""
        assignment_dict = {}
        for assignment in self.list_of_assignments[:num]:
            assign_path = self.path_to_assignments + assignment
            with open(assign_path, 'r') as f:
                text = f.read()
            
            if formatted == True:
                key = assignment.replace('.md', '')
                assignment_dict[key] = text
            else:
                assignment_dict[assignment] = text
        
        return assignment_dict
    