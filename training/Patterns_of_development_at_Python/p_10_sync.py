
from p_9_hasher import hash_file
import os
import shutil
from pathlib import Path


# Solution for sync
def reader(source):
    hashes = {}
    for folder, _, files in os.walk(source):
        for fn in files:
            hashes[hash_file(Path(folder) / fn)] = fn
    return hashes

def determine(reader_list):
    src_hashes, dst_hashes, src_folder, dst_folder = reader_list
    for sha, filename in src_hashes.items():
        if sha not in dst_hashes:
            sourcepath = Path(src_folder) / filename
            destpath = Path(dst_folder) / filename
            yield 'copy', sourcepath, destpath

        elif dst_hashes[sha] != filename:
            olddestpath = Path(dst_folder) / dst_hashes[sha]
            newdestpath = Path(dst_folder) / filename
            yield 'move', olddestpath, newdestpath

    for sha, filename, in dst_hashes.items():
        if sha not in src_hashes:
            yield 'remove', dst_folder / filename

def sync(source, dest):
    source_hashes = reader(source)
    dest_hashes = reader(dest)

    actions = determine([source_hashes, dest_hashes, source, dest])

    for action, *paths in actions:
        if action == 'move':
            shutil.copyfile(*paths)
        elif action == 'copy':
            shutil.move(*paths)
        elif action == 'remove': 
            os.remove(paths[0])

# Fake file system for test
class FakeFileSystem(list):
    def copy(self, src, dest):
        self.append(('COPY', src, dest))
    
    def move(self, src, dest):
        self.append(('MOVE', src, dest))

    def rename(self, dest):
        self.append(('DELETE', dest))

# Function for fake file system
def sync_dirs(filename, source, dest):
    actions = determine([source, dest, Path('/src'), Path('/dst')])

    for action, *paths in actions:
        if action == 'move':
            filename.move(*paths)
        elif action == 'copy':
            filename.copy(*paths)
        elif action == 'remove': 
            filename.rename(paths[0])

# Tests
def test_determine():
    src_hashes = {"hash1": "fn1"}
    dst_hashes = {}
    actions = determine([src_hashes, dst_hashes, Path('/src'), Path('/dst')])

    assert list(actions) == [('copy', Path('/src/fn1'), Path('/dst/fn1'))]

def test_determine_2():
    src_hashes = {"hash1": "fn1"}
    dst_hashes = {"hash1": "fn2"}
    actions = determine([src_hashes, dst_hashes, Path('/src'), Path('/dst')])

    assert list(actions) == [('move', Path('/dst/fn2'), Path('/dst/fn1'))]

def test_determine_3():
    src_hashes = {}
    dst_hashes = {"hash1": "fn2"}
    actions = determine([src_hashes, dst_hashes, Path('/src'), Path('/dst')])

    assert list(actions) == [('remove', Path('/dst/fn2'))]

def test_file_fake():
    filesystem = FakeFileSystem()
    
    source = {"sha1": "my-file"}
    dest = {}

    sync_dirs(filesystem, source, dest)

    source = {"sha1": "my-file"}
    dest = {"sha1": "my-file2"}

    sync_dirs(filesystem, source, dest)

    assert filesystem == [
        ('COPY', Path("/src/my-file"), Path("/dst/my-file")),
        ('MOVE', Path("/dst/my-file2"), Path("/dst/my-file"))
    ]
