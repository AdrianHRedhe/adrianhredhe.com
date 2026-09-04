## Geolocalization Stockholm

Predicting where a street-view photo was taken in Stockholm using only its pixels, by
comparing it against a gallery of images with CLIP, a general-purpose off-the-shelf embedding
model. Toggle between a smaller and larger image gallery. The gallery is drawn from a dataset
of 100K images I collected in preparation for my master's thesis.

Click the button (or reload the page) for a random query image, shown leftmost, alongside its
5 nearest neighbors from the gallery. On the map, blue dots mark those matches and the red
circle marks the query's true location. Have fun!

Source and write-up: [Stockholm-Geolocalization-Retrieval on GitHub](https://github.com/AdrianHRedhe/Stockholm-Geolocalization-Retrieval).
Also viewable directly on [Hugging Face Spaces](https://huggingface.co/spaces/AdrianHR/Geolocalization_Stockholm_Demo).

<div style="width: 100%; height: 1500px;">
<iframe src="https://geolocalization_v1.adrianhredhe.com/" width="100%" height="100%" frameborder="0"></iframe>
</div>
