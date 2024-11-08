{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a46917e7-a192-4590-b8dc-6dd9f04502ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: opencv-python-headless in c:\\users\\eng.elaf\\appdata\\roaming\\python\\python311\\site-packages (4.10.0.84)\n",
      "Requirement already satisfied: easyocr in c:\\users\\eng.elaf\\appdata\\roaming\\python\\python311\\site-packages (1.7.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (2.1.4)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (4.9.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: torch in c:\\users\\eng.elaf\\appdata\\roaming\\python\\python311\\site-packages (from easyocr) (2.4.1)\n",
      "Requirement already satisfied: torchvision>=0.5 in c:\\users\\eng.elaf\\appdata\\roaming\\python\\python311\\site-packages (from easyocr) (0.19.1)\n",
      "Requirement already satisfied: scipy in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (1.11.4)\n",
      "Requirement already satisfied: scikit-image in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (0.22.0)\n",
      "Requirement already satisfied: python-bidi in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (0.6.0)\n",
      "Requirement already satisfied: PyYAML in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (6.0.1)\n",
      "Requirement already satisfied: Shapely in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (2.0.6)\n",
      "Requirement already satisfied: pyclipper in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (1.3.0.post5)\n",
      "Requirement already satisfied: ninja in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from easyocr) (1.11.1.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: filelock in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from torch->easyocr) (3.13.1)\n",
      "Requirement already satisfied: sympy in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from torch->easyocr) (1.12)\n",
      "Requirement already satisfied: networkx in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from torch->easyocr) (3.1)\n",
      "Requirement already satisfied: fsspec in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from torch->easyocr) (2023.10.0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: imageio>=2.27 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from scikit-image->easyocr) (2.33.1)\n",
      "Requirement already satisfied: tifffile>=2022.8.12 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from scikit-image->easyocr) (2023.4.12)\n",
      "Requirement already satisfied: lazy_loader>=0.3 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from scikit-image->easyocr) (0.3)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: mpmath>=0.19 in c:\\users\\eng.elaf\\anaconda3\\lib\\site-packages (from sympy->torch->easyocr) (1.3.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit opencv-python-headless easyocr\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "46f4fa6b-3616-4880-9e23-8ae756350652",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import cv2\n",
    "import easyocr\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "\n",
    "# تحميل قارئ النصوص\n",
    "reader = easyocr.Reader(['en', 'ar'])  # يدعم الإنجليزية والعربية\n",
    "\n",
    "# إعداد واجهة المستخدم\n",
    "st.title(\"نموذج قراءة التحاليل الطبية\")\n",
    "st.write(\"يرجى تحميل صورة التحليل الطبي.\")\n",
    "\n",
    "# تحميل الصورة من المستخدم\n",
    "uploaded_image = st.file_uploader(\"تحميل الصورة\", type=[\"jpg\", \"png\", \"jpeg\"])\n",
    "\n",
    "if uploaded_image is not None:\n",
    "    # تحويل الصورة لصيغة قابلة للمعالجة\n",
    "    image = Image.open(uploaded_image)\n",
    "    image_np = np.array(image)\n",
    "\n",
    "    # عرض الصورة الأصلية\n",
    "    st.image(image, caption=\"الصورة المحملة\", use_column_width=True)\n",
    "\n",
    "    # استخراج النصوص من الصورة باستخدام EasyOCR\n",
    "    st.write(\"يتم الآن قراءة محتوى التحليل...\")\n",
    "    results = reader.readtext(image_np, detail=1)\n",
    "\n",
    "    # عرض النتائج المستخلصة\n",
    "    st.write(\"النتائج المستخلصة:\")\n",
    "    for (bbox, text, prob) in results:\n",
    "        st.write(f\"النص: {text} - الدقة: {prob:.2f}\")\n",
    "        \n",
    "        # رسم مستطيل حول النصوص المكتشفة في الصورة\n",
    "        top_left = tuple(map(int, bbox[0]))\n",
    "        bottom_right = tuple(map(int, bbox[2]))\n",
    "        cv2.rectangle(image_np, top_left, bottom_right, (0, 255, 0), 2)\n",
    "\n",
    "    # عرض الصورة مع المستطيلات\n",
    "    st.image(image_np, caption=\"الصورة مع النصوص المستخلصة\", use_column_width=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8bfca0c5-734e-487b-af6b-12375e899a16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
