from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def write(self):

        pass

    @abstractmethod
    def debug(self):

        pass

    @abstractmethod
    def execute(self):

        pass


class Vscode(Editor):

    def open(self):

        print("VSCODE OPEN METHOD")

    def write(self):

        print("VSCODE WRITE METHOD")

    def debug(self):

        print("VSCODE DEBUG METHOD")

    def execute(self):

        print("VSCODE EXECUTE METHOD")


vs_instance=Vscode()

vs_instance.open()

vs_instance.execute()