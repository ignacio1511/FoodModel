import React, {useState} from 'react'
import S3 from 'react-aws-s3';
import { MdAddAPhoto } from "react-icons/fa";
import { FaCamera } from 'react-icons/fa';


export default function Hero() {


  const [file, setFile] = useState('')

  const config = {
    bucketName: 'foodmodelbucket',
    region: 'us-east-1',
    accessKeyId: 'AKIA32DKVD47H5NQKQ6R',
    secretAccessKey: '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',
}

const ReactS3Client = new S3(config);

// ReactS3Client
//     .uploadFile(file, newFileName)
//     .then(data => console.log(data))
//     .catch(err => console.error(err))


const handleSubmit = (e) => {
  e.preventDefault();
  const file = {file};

  fetch('http://127.0.0.1:8000/api/user-create/', {
      method : 'POST',
      headers: {"Content-Type" : "application/json"},
      body: JSON.stringify(usuario),
  }). then(() => {
      console.log("Nuevo usuario añadido")
      console.log(usuario)
  })

  router.push('/thank-you')
} 

  return (
    <>
    <div className="wrapper container-fluid -mt-0">
    <h1 className='text-center text-3xl'>¿Que comerás hoy?</h1>
    <p className='text-center text-s mt-3'>Toma una foto de tu comida y súbela para ver su información nutricional.</p>

    <label className="block mt-4">
      <form onSubmit={handleSubmit}>

          <input type="file" 
          required 
          name="first_name" 
          className="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" 
          value={file} 
          onChange={(e) => setFile(e.target.value)}
          />
      </form>
    </label>
    
    <div className='grid grid-cols-2'>
    <h1 className='text-black text-center'>1. Sube una foto</h1>
    <h1 className='text-black text-center'>2. Obten su Información Nutricional</h1>
    </div>

    <div className='grid grid-cols-2 mt-3'>
    <section className='bg-orange-500 w-full pb-40 pt-40'>
    </section>
    <section className='bg-orange-200 w-full pb-40 pt-40'>
    </section>
    </div>
    </div>

  </>
  )
}
