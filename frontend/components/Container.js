import Head from 'next/head'
import Navbar from './Navbar';
import Footer from './Footer'


const Container = ({titulo,children}) =>(
    
    <div>
        <Head>
        <link rel="shortcut icon" href="/images/favicon.ico"/>
        <title>{titulo}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://kit.fontawesome.com/448126ce4f.js" crossOrigin="anonymous"></script>
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
        <link rel="stylesheet" type="text/css" href="https://s3.amazonaws.com/static.mlh.io/blog-code/2018-02-clarifai-nutrition-app/app.css" />
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossOrigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/united/bootstrap.min.css" />            
        </Head>
        <Navbar/>
        <div>
            {children}
        </div>
        <Footer/>
    </div>
)
export default Container;