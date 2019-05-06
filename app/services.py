def call(path, name, version, data):
    m = getattr(__import__('apis.{}.{}'.format(version, path), fromlist=['']), name)
    return m(data)
