from pypdf import PdfWriter 
import os  
  
def merge_chapters(output_file, start=1, end=7):  
    merger = PdfWriter()  
    for i in range(start, end):  # Chapters start to end-1  
        filename = f'chapter ({i}).pdf'  
        if os.path.exists(filename):  
            merger.append(filename)  
            print(f"Added {filename}")  
        else:  
            print(f"File {filename} not found")  
    merger.write(output_file)  
    merger.close()  
    print(f"Merged chapters {start} to {end-1} into {output_file}")  
  
# Merge chapters 1 to 6  
merge_chapters('merged_chapters.pdf', 1, 7) 
