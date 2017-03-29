from werkzeug.serving import run_simple
from werkzeug.wrappers import BaseRequest, BaseResponse
from werkzeug.wsgi import wrap_file

def view_file(request):
    if not 'uploaded_file' in request.files or not request.files['uploaded_file'].filename:
        return BaseResponse('no file uploaded')
    f = request.files['uploaded_file']
    return BaseResponse(wrap_file(request.environ, f), 
                        mimetype=f.content_type,
                        direct_passthrough=True)
            
def upload_file(request):
    return BaseResponse('''
            <h1>Upload File</h1>
            <form action="" method="post" enctype="multipart/form-data">
                <input type="file" name="uploaded_file">
                <input type="submit" value="Upload">
            </form>''', 
            mimetype='text/html')
            
def application(environ, start_response):
    request = BaseRequest(environ)
    if request.method == 'POST':
        response = view_file(request)
    else:
        response = upload_file(request)
    return response(environ, start_response)
    
run_simple('', 8000, application)