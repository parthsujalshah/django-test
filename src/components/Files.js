import React, { useState } from 'react';

const Files = props => {

    const [title, setTitle] = useState("");
    const [cover, setCover] = useState();

    const newBook = () => {
        console.log(title);
        console.log(cover);
        console.log(typeof cover);

        const uploadData = new FormData();
        uploadData.append('title', title);
        uploadData.append('file', cover, cover.name);

        fetch('http://127.0.0.1:8000/api/files/files/', {
            method: 'POST',
            body: uploadData
        })
            .then(res => console.log(res))
            .catch(err => console.log(err));
    };

    return (
        <div>
            <h3>Upload Files with react</h3>
            <label>
                Title
            <input type="text" value={title} onChange={event => setTitle(event.target.value)} />
            </label>
            <label>
                Cover
            <input type="file" onChange={event => {
                    setCover(event.target.files[0]);
                }} />
            </label>
            <br />
            <button onClick={() => newBook()}>New Book</button>
        </div>
    );
};

export default Files;