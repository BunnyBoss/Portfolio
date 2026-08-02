import { motion } from "framer-motion";
import { heroContent } from "../constants";
import { HeroCanvas } from "./canvas";

const Hero = () => {
  return (
    <section className="relative w-full h-screen mx-auto">
      {/* 3D Background */}
      <div className="absolute inset-0 z-0">
        <HeroCanvas />
      </div>

      {/* Content overlay */}
      <div className="absolute inset-0 z-10 sm:px-16 px-6 flex flex-row items-center justify-start max-w-7xl mx-auto pointer-events-none">
        <div className="flex flex-col items-start gap-5">
          {/* Accent bar — warm moonlit gold */}
          <div className="flex flex-col justify-center items-center mt-5">
            <div className="w-5 h-5 rounded-full bg-accent-secondary" />
            <div className="w-1 sm:h-80 h-40 bg-gradient-to-b from-accent-secondary to-transparent" />
          </div>
        </div>

        <div className="ml-4 pointer-events-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <h1 className="font-heading font-black text-white lg:text-[72px] sm:text-[56px] xs:text-[44px] text-[36px] lg:leading-[88px] mt-2">
              {heroContent.greeting}{" "}
              <span className="text-accent-secondary drop-shadow-[0_0_15px_rgba(212,165,116,0.4)]">{heroContent.name}</span>
            </h1>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.5 }}
          >
            <p className="text-secondary font-medium lg:text-[28px] sm:text-[24px] xs:text-[20px] text-[18px] lg:leading-[36px] mt-2">
              {heroContent.tagline}
            </p>
          </motion.div>

          <motion.p
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.8 }}
            className="mt-4 text-secondary/80 max-w-[600px] text-[15px] leading-[26px]"
          >
            {heroContent.description}
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.1 }}
            className="flex gap-4 mt-6"
          >
            <a
              href="#contact"
              className="bg-accent-secondary hover:bg-accent-secondary/80 text-primary font-bold py-3 px-8 rounded-xl transition-all hover:shadow-lg hover:shadow-accent-secondary/25"
            >
              Get in Touch
            </a>
            <a
              href="#works"
              className="border border-accent/30 text-accent hover:bg-accent/10 font-medium py-3 px-8 rounded-xl transition-all"
            >
              View Projects
            </a>
          </motion.div>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute xs:bottom-10 bottom-32 w-full flex justify-center items-center z-10">
        <a href="#about">
          <div className="w-[35px] h-[64px] rounded-3xl border-4 border-secondary/40 flex justify-center items-start p-2">
            <motion.div
              animate={{ y: [0, 24, 0] }}
              transition={{ duration: 1.5, repeat: Infinity, repeatType: "loop" }}
              className="w-3 h-3 rounded-full bg-accent mb-1"
            />
          </div>
        </a>
      </div>
    </section>
  );
};

export default Hero;
