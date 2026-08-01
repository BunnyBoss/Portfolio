import { BrowserRouter } from "react-router-dom";
import {
  About,
  Contact,
  Experience,
  Hero,
  Navbar,
  Tech,
  Works,
  StarsCanvas,
  MoonOverlayCanvas,
  Footer,
  CustomCursor,
} from "./components";

const App = () => {
  return (
    <BrowserRouter>
      <CustomCursor />
      <div className="relative z-0 bg-transparent">
        <div className="bg-cover bg-no-repeat bg-center bg-primary">
          <Navbar />
          <Hero />
        </div>
        <div className="relative z-0">
          <MoonOverlayCanvas />
          <StarsCanvas />
          <About />
          <Experience />
          <Tech />
          <Works />
          <Contact />
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
};

export default App;
