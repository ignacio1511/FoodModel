

const Navbar =()=> {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark lg:pb-0 md:pb-1 sm:pb-1" style={{backgroundColor: '#1c1c1c'}}>
        <div className="container-fluid -mt-2 mb-1">
        <a href="/"><img src="images/seiken-logo-text.png" alt="" width={100} height={100}/></a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"/>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link">Inicio</a>
              </li>
              <li className="nav-item">

              <a className="nav-link">Mi cuenta</a>
               
              </li>
            </ul>
            
            {/* <button type="button" class="btn btn-primary bg-orange-700" data-toggle="button" aria-pressed="false" autocomplete="off">Iniciar sesion</button> */}
          </div>
        </div>
      </nav>
    )
}
export default Navbar;