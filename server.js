const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
// const { processResume } = require('./processResume'); // Make sure this is implemented

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());
app.use(express.json());
app.use('/favicon.ico', express.static('path/to/your/favicon.ico'));

// Add a route for the root URL
app.get('/', (req, res) => {
  res.send('Welcome to the resume processing API!');
});

// Endpoint for uploading and processing the resume
app.post('/api/upload_resume', upload.single('file'), (req, res) => {
  const filePath = req.file.path;

  // Call your function to extract skills from the resume
  const skills = processResume(filePath); // Make sure processResume is defined and implemented

  res.json({ skills });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
