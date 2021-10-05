import subprocess


def process(source=None, destination=None):
    if source is None and destination is None:
        subprocess.call(["sigal", "build"])
    
    elif source is None:    
        subprocess.call(["sigal", "build", destination])
    
    elif destination is None:
        subprocess.call(["sigal", "build", source])

    else:
        subprocess.call(["sigal", "build", source, destination])


if __name__ == "__main__":
    process()

