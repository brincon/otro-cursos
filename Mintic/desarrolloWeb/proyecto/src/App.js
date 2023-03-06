import logo from './media/logo.png';
import './styles/styles.css';
import borderCollie from './media/borderCollie.png'

function App() {
  return (
    <div className="App">
          <header>
        <ul className="navbar">
            <li>
                <img src={logo} alt="image" className="logo" />
            </li>
            <li><button className="button mainButton">Nuevo post</button></li>
            <li>
                <div className="buscar">
                    <input placeholder="Buscar una raza"/>
                    <i className="fa-solid fa-magnifying-glass"></i>
                </div>
            </li>
            <li><button className="button secundaryButton">login</button></li>
            <li><button className="button mainButton">Registro</button></li>
            
         
        </ul>
    </header>
    <main>
        <section></section>
        <section></section>
    </main>
    <footer></footer>
    </div>
  );
}

export default App;
