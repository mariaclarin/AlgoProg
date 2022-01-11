class Person:
    def __init__(self, name :str, address : str ):
        self.__name = name 
        self.__address = address
    
    def getName(self) -> str:
        return self.__name
    
    def getAddress(self) -> str:
        return self.__address
    
    def setAddress(self, address : str ) -> None:
        self.__address = address
    
    def __str__(self) -> str:
        return f"{self.getName()}({self.getAddress()})"
    
class Student(Person):
    def __init__(self, name, address) :
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = {}
        self.__grades = {}
    
    def addCourseGrade(self, course : str, grade :int) -> None:
        pass

    def printGrades(self) -> None :
        pass

    def getAverageGrade(self) -> float :
        pass
    
    def __str__(self)->str:
        return f"Student : {self.getName()}({self.getAddress()})"

class Teacher(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = {}
    
    def addCourse(self, course : str)-> bool:
        pass
    
    def removeCourse(self, course : str)-> bool:
        pass
    
    def __str__(self) -> str:
        return f"Teacher : {self.getName()}({self.getAddress()})"


    
