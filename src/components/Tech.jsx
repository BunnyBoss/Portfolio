import { motion } from "framer-motion";
import { technologies } from "../constants";
import { textVariant, fadeIn } from "../utils/motion";
import SectionWrapper from "../hoc/SectionWrapper";

const TechBall = ({ name, icon, index }) => (
  <motion.div
    variants={fadeIn("up", "spring", index * 0.1, 0.5)}
    className="flex flex-col items-center group"
  >
    <div className="w-24 h-24 rounded-full glass-card flex items-center justify-center cursor-pointer
      transition-all duration-300 group-hover:shadow-lg group-hover:shadow-accent/30
      group-hover:border-accent/50 border border-white/5 pulse-glow"
    >
      <span className="text-4xl">{icon}</span>
    </div>
    <p className="text-secondary text-[12px] mt-2 text-center group-hover:text-white transition-colors">
      {name}
    </p>
  </motion.div>
);

const Tech = () => {
  return (
    <>
      <motion.div variants={textVariant()}>
        <p className="sm:text-[18px] text-[14px] text-secondary uppercase tracking-wider">
          My technical toolkit
        </p>
        <h2 className="text-white font-black md:text-[60px] sm:text-[50px] xs:text-[40px] text-[30px]">
          Technologies.
        </h2>
      </motion.div>

      <div className="mt-16 flex flex-row flex-wrap justify-center gap-10">
        {technologies.map((tech, index) => (
          <TechBall key={tech.name} index={index} {...tech} />
        ))}
      </div>
    </>
  );
};

export default SectionWrapper(Tech, "tech");
