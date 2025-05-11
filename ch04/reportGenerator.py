from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def generate(self):
        self.header()
        content = self.generate_content()
        self.export(content)

    def header(self):
        print(f"==== {self.title} ====")

    @abstractmethod
    def generate_content(self):
        pass

    @abstractmethod
    def export(self, content):
        pass


class PdfReport(ReportGenerator):
    def generate_content(self):
        return "\n".join([f"- {item}" for item in self.data])

    def export(self, content):
        print("[PDF Report]")
        print(content)

class HtmlReport(ReportGenerator):
    def generate_content(self):
        return "<ul>"+ "".join(f"<li>{item}<li>" for item in self.data)+ "</ul>"

    def export(self, content):
        print("[HTML Report]")
        print(content)

r1 = PdfReport("sales report", ["Apples: 100","Bananas: 80"])
r1.generate()

h1 = HtmlReport("[HTML] Report", ["News: Electric car", "News: Trunk"])
h1.generate()
