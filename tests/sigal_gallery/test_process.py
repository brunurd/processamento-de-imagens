import os
from sigal_gallery.process import process


def test_process():
    process(source="/home/ubuntu/pezaoshow/sigal_gallery/tests/mocks/src",
            destination="/home/ubuntu/pezaoshow/sigal_gallery/tests/mocks/dest")

    generated_files = []

    for root, _, files in os.walk("tests/mocks/dest/gatinhos"):
        for name in files:
            generated_files.append(os.path.join(root, name))

    assert "tests/mocks/dest/gatinhos/4096.png" in generated_files
    assert "tests/mocks/dest/gatinhos/1080.jpeg" in generated_files
    assert "tests/mocks/dest/gatinhos/200.png" in generated_files
