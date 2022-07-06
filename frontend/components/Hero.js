import { data } from 'jquery';
import React, {useState} from 'react'
import S3 from 'react-aws-s3';


export default function Hero() {

  const [selectedFile, setSelectedFile] = useState('');

  const config = {
    bucketName: process.env.NEXT_PUBLIC_BUCKET_NAME,
    region: process.env.NEXT_PUBLIC_REGION,
    accessKeyId: process.env.NEXT_PUBLIC_ACCESS,
    secretAccessKey: process.env.NEXT_PUBLIC_SECRET,
    s3Url: "https://foodmodelbucket.s3.amazonaws.com",
  }

  const handleFileInput = (e) => {
    setSelectedFile(e.target.files[0]);
  }


  const uploadFile = async (file) => {
    const ReactS3Client = new S3(config);
    ReactS3Client
    .uploadFile(file, file.name)
    .then(data => fetch('http://127.0.0.1:8000/api/image-create/', {
      method : 'POST',
      headers: {"Content-Type" : "application/json"},
      body: JSON.stringify({image_url:data.location}),
  }). then(() => {
      console.log("Nueva imagen añadida")
      console.log({image_url:data.location})})
  )
    .catch(err => console.error(err))
  }

  // const handleSubmit = (e) => {
  //   e.preventDefault();e.preventDefault();
  //   const file = {file};



  return (
    <>
    <div className="wrapper container-fluid -mt-0">
    <h1 className='text-center text-3xl'>¿Que comerás hoy?</h1>
    <p className='text-center text-s mt-3'>Toma una foto de tu comida y súbela para ver su información nutricional.</p>


    <div className="h-56 grid grid-cols-1 gap-3 content-center">
        <input className="mt-3" type="file" onChange={handleFileInput}/>
        <br></br>
        <button className="mx-10 mt-3 mb-4 btn btn-primary bg-orange-700" onClick={() => uploadFile(selectedFile)}> Obtener Información Nutricional</button>
    </div>
    <div className='grid grid-cols-2'>
    <h1 className='text-black text-center'>1. Sube una foto</h1>
    <h1 className='text-black text-center'>2. Obten su Información Nutricional</h1>
    </div>

    <div className='grid grid-cols-2 mt-3'>
    <section className='bg-orange-500 w-full pb-40 pt-40'>
      
    <img src ={`https://foodmodelbucket.s3.amazonaws.com/${selectedFile.name}`}/>
    <h1>{`https://foodmodelbucket.s3.amazonaws.com/${selectedFile.name}`} </h1>
    </section>
    <section className='bg-orange-200 w-full pb-40 pt-40'>
    </section>
    </div>
    </div>

  </>
  )
}
