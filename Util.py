import os
import zipfile

def zipDir(inputPath, outputFile):
    # ziph is zipfile handle
    ziph = zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(outputFile, '..')))
    ziph.close()