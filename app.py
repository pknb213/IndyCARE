from utils import *
from apis import *
from views import *

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000)