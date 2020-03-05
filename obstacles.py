{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import copy\n",
    "import math\n",
    "import matplotlib.pyplot as plt\n",
    "#from dataclasses import dataclass, field\n",
    "np.set_printoptions(threshold=np.inf)\n",
    "import argparse\n",
    "import cv2\n",
    "from itertools import cycle\n",
    "\n",
    "def InitCanvas(width, height, color=(255, 255, 255)):\n",
    "    canvas = np.ones((height, width, 3), dtype=\"uint8\")\n",
    "    canvas[:] = color\n",
    "    return canvas\n",
    "\n",
    "canvas = InitCanvas(300, 200, color=(255,255,255))\n",
    "\n",
    "\n",
    "cv2.circle(canvas,(225,50),25,(0,0,0))\n",
    "\n",
    "cv2.ellipse(canvas,(150,100),(40,20),0,0,360, (0,0,0))\n",
    "\n",
    "Recpoints = np.array([[95,170],[100,161],[35,124],[30,133]], np.int32)\n",
    "\n",
    "Polypoints = np.array([[20,80],[50,50],[75,80],[100,50],[75,15],[25,15]],np.int32)\n",
    "\n",
    "Diapoints= np.array([[225,190],[250,175],[225,160],[200,175]], np.int32)\n",
    "\n",
    "\n",
    "cv2.polylines(canvas, pts=[Recpoints], isClosed=True, color=(0,0,0))\n",
    "cv2.polylines(canvas, pts=[Polypoints], isClosed=True, color=(0,0,0))\n",
    "cv2.polylines(canvas, pts=[Diapoints], isClosed=True, color=(0,0,0))\n",
    "\n",
    "cv2.imshow(\"obstacles\", canvas)\n",
    "cv2.imwrite(\"obstacles.png\", canvas)\n",
    "\n",
    "cv2.waitKey(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
