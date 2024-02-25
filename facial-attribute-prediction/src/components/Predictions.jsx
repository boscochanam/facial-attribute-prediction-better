import React from 'react';

const Predictions = ({ data }) => {
  // Check if data is null or undefined
  if (!data) {
    console.log(data + " is the prediction");
    return <div>No predictions available</div>;
  } else {
    console.log(data + " is the prediction");
  }

  // Destructure data object
  const { Age, Gender, Ethnicity } = data;

  // Convert Ethnicity object to a string for display
  // const ethnicityString = Object.entries(Ethnicity).map(([key, value]) => (
  //   <p key={key}>{key}: {value}%</p>
  // ));

  return (
    <div>
      <h2>Prediction Results</h2>
      <p><strong>Age:</strong> {Age}</p>
      <p><strong>Gender:</strong> {Gender}</p>
      {/* <div><strong>Ethnicity:</strong> {ethnicityString}</div> */}
    </div>
  );
};

export default Predictions;
