from compiler import create_image
from ia_parser import parse_ndjson
import os

def _ensure_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def _ensure_path_exists(path):
    splitted = path.split('/')
    for i in range(len(splitted)):
        _ensure_exists('/'.join(splitted[:i+1]))
    print('created path: {}'.format(path))

def _summary(state):
    train = state['train']
    test = state['test']
    unrec = state['unrecognized']
    return '{} images processed:\n+ {} selected to train\n+ {} selected to test\n + {} skipped'.format(
        train + test + unrec,
        train,
        test,
        unrec
    )
    
def split_train_test(filepath, train_ratio, test_ratio):
    total = train_ratio + test_ratio
    drawings = parse_ndjson(filepath)

    _ensure_path_exists('images/train/{}'.format(drawings[0]['word']))
    _ensure_path_exists('images/test/{}'.format(drawings[0]['word']))
    
    state = {
        'train': 0,
        'test': 0,
        'unrecognized': 0,
        'state': 0,
    }
    
    for d in drawings:
        if not d['recognized']:
            state['unrecognized'] += 1
            continue
        
        subfolder = {
            True: 'test',
            False: 'train',
        }[state['state'] >= train_ratio]
        
        state[subfolder] += 1
        state['state'] = (state['state'] + 1) % total
        
        create_image(d['drawing'], 'images/{}/{}/{}.jpg'.format(subfolder, d['word'], d['key_id']))
        
    print(_summary(state))
        
        