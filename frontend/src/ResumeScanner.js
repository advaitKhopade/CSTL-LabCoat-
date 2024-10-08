import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ResumeScanner = () => {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setText(event.target.result);
      };
      reader.readAsText(file);
    }
  }, [file]);

  useEffect(() => {
    if (text) {
      const skills = extractSkillsFromText(text);
      setSkills(skills);
    }
  }, [text]);

  const extractSkillsFromText = (text) => {
    // Implement your skill extraction logic here
    // For example, you can use a library like natural or a simple regex
    const skills = text.match(/(javascript|react|node|python|java)/gi);
    return skills;
  };

  return (
    <div>
      <h2>Resume Scanner</h2>
      <p>{text}</p>
      <ul>
        {skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
};

export default ResumeScanner;