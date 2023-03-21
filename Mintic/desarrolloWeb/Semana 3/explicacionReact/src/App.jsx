import 'styles/styles.css';
import logo from 'media/logo.png';
import borderCollie from 'media/borderCollie.jpg';
import rhodesian from 'media/rhodesian.jpg';
import CardRazasPerros from 'components/cardRazasPerros';

function App() {
  return (
    <div className="App">
          <header>
        <ul className="navbar">
            <li>
                <img src={logo} alt="image" className="logo"/>
            </li>
            <li><button className="botonGenerico mainButton">Nuevo post</button></li>
            <li>
                <div className="buscar">
                    <input placeholder="Buscar una raza"/>
                    <i className="fa-solid fa-magnifying-glass botonGenerico iconoBusqueda"></i>
                </div>
            </li>
            <li><button className="botonGenerico secundaryButton">login</button></li>
            <li><button className="botonGenerico mainButton">Registro</button></li>
            
         
        </ul>
    </header>
    <main>
        <section>
            <h1>Razas de perros</h1>
            <ul className="breedCardContainer">
                <CardRazasPerros nombreRaza="Border Collie" imagen ={borderCollie}/>
                <CardRazasPerros nombreRaza="Rhodesian" imagen ={rhodesian}/>           
            </ul>
        </section>
        <section></section>
    </main>
    <footer></footer>
    </div>
  );
}

export default App;
