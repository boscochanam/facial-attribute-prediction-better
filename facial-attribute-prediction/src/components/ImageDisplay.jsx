import React, { useState } from 'react';
import Predictions from './Predictions';

const ImageDisplay = () => {
    const [image, setImage] = useState(null);
    const [predictions, setPredictions] = useState([]);
    const [file, setFile] = useState(null);

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = () => {
            setImage(reader.result);
        };

        if (file) {
            reader.readAsDataURL(file);
            setFile(file);
        }
    };

    const handlePrediction = () => {
        console.log(file);
        if (file) {
            const formData = new FormData();
            formData.append('image', file);

            console.log(image);
            console.log(formData.get('image'));
            fetch('http://127.0.0.1:5000/pic-send', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    // Handle the response data
                })
                .catch(error => {
                    // Handle the error
                });
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '70vh' }}>
            <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', alignItems: 'center', gap: '80px' }}>
                {image && <img src={image} alt="Uploaded Image" style={{ objectFit: 'cover', height: '400px', width: '400px', marginBottom: '20px'}} />}
                {image && <Predictions data={predictions} />}  
            </div>
            <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', alignItems: 'center', gap: '10px' }}>
                <button onClick={() => document.getElementById('imageUpload').click()} style={{ marginTop: '20px', backgroundColor: 'green', color: 'white' }}>Upload Image</button>
                <input id="imageUpload" type="file" accept="image/*" onChange={handleImageUpload} style={{ display: 'none' }} />
                {image && <button onClick={() => setImage(null)} style={{ marginTop: '20px', backgroundColor: 'red', color: 'white' }}>Clear Image</button>}
            </div>
            {image && <button onClick={handlePrediction} style={{ marginTop: '20px', backgroundColor: 'blue', color: 'white' }}>Predict</button>}
        </div>
    );
};

export default ImageDisplay;
