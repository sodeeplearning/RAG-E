from os import listdir
from os.path import join
import os
import zipfile
import io
from fastapi import Response


def getting_files(link):
    return [join(link, f) for f in listdir(link)]


def zipfiles(filenames):
    zip_filename = "archive.zip"
    s = io.BytesIO()
    zf = zipfile.ZipFile(s, "w")
    for fpath in filenames:
        fdir, fname = os.path.split(fpath)
        zf.write(fpath, fname)

    zf.close()

    resp = Response(s.getvalue(), media_type="application/x-zip-compressed", headers={
        'Content-Disposition': f'attachment;filename={zip_filename}'
    })
    return resp
