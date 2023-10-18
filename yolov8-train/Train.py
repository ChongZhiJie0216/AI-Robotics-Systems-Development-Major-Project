from ultralytics import YOLO

# Load a model
model = YOLO("/home/ChongZhiJie/Desktop/AI-Robotics-Systems-Development-Major-Project/yolov8/yolov8n.yaml")  # build a new model from scratch
model = YOLO("/home/ChongZhiJie/Desktop/AI-Robotics-Systems-Development-Major-Project/yolov8/yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="/home/ChongZhiJie/Desktop/AI-Robotics-Systems-Development-Major-Project/yolov8/coco128.yaml", epochs=30)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format