from tkinter import filedialog

class Importer:
    def __init__(self):
        pass
    def import_file(self,file_path):
        try:
            with open(file_path,encoding='utf-8') as f:
                return f.read()
        except OSError:
            return "File not found"

    def export_file(self,text):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text File",".txt")])
        if file_path:
            with open(file_path,'w',encoding='utf-8') as f:
                f.write(text)
        if not file_path:
            return
