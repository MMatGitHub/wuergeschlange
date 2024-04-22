import tempfile
import os
import protokolliere
def test_availability(path):
    try:
        with open(os.path.join(path, 'test.txt'), 'w') as f:
            f.write('Testing folder availability...')
        os.remove(os.path.join(path, 'test.txt'))
        protokolliere.ok(f"i: Availability OK: [{path}]")
        return True
    except Exception as e:
        protokolliere.debug(f"Error while testing availability of [{path}], error: [{e}]")
        raise e
        return False