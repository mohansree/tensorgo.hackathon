# tensorgo.hackathon
Code for the hackathon conducted by TensorGo.

## Design

```python
'''Main module.
Invoke run.

Usage:
    Run as it is.
'''
import typing

import hackathon

person_detector_pretrained: str = "models/person_detector"
person_reid_pretrained: str = "models/person_reid"
face_detector_pretrained: str = "models/face_detector"
mask_identifier_pretrained: str = "models/mask_identifier"
device: int = 0
iteration: int = 1e+10

video: hackathon.Video = hackathon.Video(device=device,)
person_detector: hackathon.PersonDetector = (
    hackathon.PersonDetector.from_pretrained(person_detector_pretrained))
person_reid: hackathon.PersonReid = (
    hackathon.PersonReid.from_pretrained(person_reid_pretrained))
pid_displayer: hackathon.PIDDisplayer = (
    hackathon.PIDDisplayer()
)
face_detector: hackathon.FaceDetector = (
    hackathon.FaceDetector.from_pretrained(face_detector_pretrained)
)
mask_identifier: hackathon.MaskIdentifier = (
    hackathon.MaskIdentifier.from_pretrained(mask_identifier_pretrained)
)
mask_status_displayer: hackathon.MaskStatusDisplayer = (
    hackathon.MaskDisplayer()
)
distance_calculator: hackathon.DistanceCalculator = (
    hackathon.DistanceCalculator()
)
distance_alerter: hackathon.DistanceAlerter = (
    hackathon.DistanceAlerter()
)
runner: hackathon.Runner = hackathon.Runner()

video.start()

runner.video: hackathon.Video = video
runner.person_detector: hackathon.PersonDetector = person_detector
runner.person_reid: hackathon.PersonReid = person_reid
runner.pid_displayer: hackathon.PIDDisplayer = pid_displayer
runner.face_detector: hackathon.FaceDetector = face_detector
runner.mask_identifier: hackathon.MaskIdentifier = mask_identifier
runner.mask_status_displayer: hackathon.MaskStatusDisplayer = mask_status_displayer
runner.distance_calculator: hackathon.DistanceCalculator = distance_calculator
runner.distance_alerter: hackathon.DistanceAlerter = distance_alerter

list(map(runner, range(iteration)))
```

```python
#runner

import typing

class Runner:
    def __call__(self,):
        frame: hackathon.Frame = self.video.get_frame()
        persons: typing.List[hackathon.Person] = self.person_detector.detect(frame)
        ids: typing.List[hackathon.Id] = list(map(self.person_reid.assign, persons))
        faces: typing.List[hackathon.Face] = list(self.face_detector.detect, persons)
        masks: typing.List[hackathon.Mask] = list(self.mask_identifier.identify, faces)
        pairs: typing.List[hackathon.Pair] = self.make_pair(persons)
        distances: typing.List[hackathon.Distance] = list(map(self.distance_calculator.calculate, persons))

        self.pid_displayer(ids)
        self.mask_status_displayer(masks)