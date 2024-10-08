const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
//const { processResume } = require('./processResume'); // Import your resume processing logic

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());
app.use(express.json());

app.post('/api/upload_resume', upload.single('file'), (req, res) => {
  const filePath = req.file.path;

  // Call your function to extract skills from the resume
  const skills = processResume(filePath); // Implement this function to return an array of skills

  res.json({ skills });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
