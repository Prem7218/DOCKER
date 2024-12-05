const fs = require("fs");

// File to read
const filePath = "./data.txt";

// Read the file and display its content
fs.readFile(filePath, "utf-8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err.message);
    return;
  }
  console.log("File Content:\n", data);
});
