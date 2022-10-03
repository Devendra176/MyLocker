from rest_framework.response import Response


def ResponseGenerator(data, status, is_valid=None, message=None, errors=None):

    data.update({
        'status': status,
        'is_valid': is_valid,
    })

    if message:
        data.update({'message': message})

    if not is_valid:
        data.update({
            'errors': errors,
        })
        return Response(data,status)
    
    return Response(data, status)
