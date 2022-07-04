import wolframalpha
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
wolfram_client = wolframalpha.Client("KAUE7Y-W9JK9EX9Q5")

CLARIFAI_API_KEY = "d8b45673fe61436ca006239d65426472"
APPLICATION_ID = "foodModelv2"
IMAGE_URL = "https://www.quimicaysociedad.org/wp-content/uploads/2015/06/platano.jpg"

## S3 AWS

metadata = (("authorization", f"Key {CLARIFAI_API_KEY}"),)

request = service_pb2.PostModelOutputsRequest(
    model_id="food-item-v1-recognition",
    user_app_id=resources_pb2.UserAppIDSet(app_id=APPLICATION_ID),
    inputs=[resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=IMAGE_URL)))],
)
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
    print(response)
    raise Exception(f"Request failed, status code: {response.status}")


alimentos_presentes = []

for concept in response.outputs[0].data.concepts:
    if concept.value > 0.99:
        print("%12s: %.2f" % (concept.name, concept.value))
        if concept.name == "chicken":
            concept.name = str(concept.name) + " breast"
        alimentos_presentes.append(concept.name)

print(alimentos_presentes)


while True:
    for alimento in alimentos_presentes:
        query = alimento
        print(alimento)
        res = wolfram_client.query(query)
        output = next(res.results).text
        print(output)
    break
