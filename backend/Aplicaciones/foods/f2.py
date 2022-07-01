import os

env = environ.Env()
environ.Env.read_env()


model_id = env("MODEL_ID")
app_id = env("APP_ID")
clarifai_api_key = env("CLARIFAI_API_KEY")
wolfram_api_key = env("WOLFRAM_API_KEY")
image_url = image_url

    def imageClassifier(self):
        metadata = (("authorization", f"Key {self.clarifai_api_key}"),)
        request = service_pb2.PostModelOutputsRequest(
            model_id=self.model_id,
            user_app_id=resources_pb2.UserAppIDSet(app_id=self.app_id),
            inputs=[resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=self.image_url)))],
        )

    def getNutritionalInfo(self):
        pass


request = service_pb2.PostModelOutputsRequest(
    model_id="food-item-v1-recognition",
    user_app_id=resources_pb2.UserAppIDSet(app_id=APPLICATION_ID),
    inputs=[resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=IMAGE_URL)))],
)
