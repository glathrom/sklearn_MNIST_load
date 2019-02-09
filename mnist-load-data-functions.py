
import struct
import numpy as np

def read_labels( path_ ):
    
    with open(path_, 'rb') as fp:
        magic = struct.unpack('>I', fp.read(4))
        number = struct.unpack('>I', fp.read(4))

        print('Number of Entries: %d' % number)

        train_labels = list()
        byte = fp.read(1)
        while byte:
            train_labels.append( int.from_bytes(byte, byteorder='big', signed=False) )
            byte = fp.read(1)
    
    return train_labels


def read_images(path_):
    with open(path_, 'rb') as fp:
        magic = struct.unpack('>I', fp.read(4))[0]
        number_images = struct.unpack('>I', fp.read(4))[0]
        rows = struct.unpack('>I', fp.read(4))[0]
        columns = struct.unpack('>I', fp.read(4))[0]

        print('Images: %d\nRows = %d\nColumns %d' % (number_images, rows, columns))

        byte = fp.read(1)
        buffer = list()
        while byte:
            buffer.append( int.from_bytes(byte, byteorder='big', signed=False ) )
            byte = fp.read(1)
    print('Loading of Images Complete')
    
    images = list()
    for t in range(number_images):
        image = buffer[rows*columns*t: rows*columns*(t+1)]
        images.append(np.array(image))
    
    return {'number_images':number_images, 'rows':rows, 'columns':columns, 'images':images}


