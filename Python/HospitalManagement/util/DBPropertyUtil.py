def getPropertyString(file_name):
    props = {}
    with open(file_name, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                props[key.strip()] = value.strip()
    return ';'.join([f"{k}={v}" for k, v in props.items()])
