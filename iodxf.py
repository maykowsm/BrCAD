import ezdxf


def inputDxf(path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    return msp
