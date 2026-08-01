import { motion } from "framer-motion";
import Tilt from "react-parallax-tilt";
import { aboutCards } from "../constants";
import { fadeIn, textVariant } from "../utils/motion";
import SectionWrapper from "../hoc/SectionWrapper";

const ServiceCard = ({ index, title, icon, description }) => (
  <Tilt
    className="xs:w-[250px] w-full"
    tiltMaxAngleX={15}
    tiltMaxAngleY={15}
    glareEnable={true}
    glareMaxOpacity={0.2}
    glarePosition="all"
    glareBorderRadius="20px"
  >
    <motion.div
      variants={fadeIn("right", "spring", index * 0.5, 0.75)}
      className="w-full p-[1px] rounded-[20px] shadow-card hover:shadow-[0_0_20px_rgba(0,229,255,0.3)] transition-shadow duration-300"
      style={{
        background: "linear-gradient(135deg, #00e5ff 0%, #111111 50%, #9d4edd 100%)",
      }}
    >
      <div className="bg-tertiary rounded-[20px] py-8 px-6 min-h-[320px] flex justify-evenly items-center flex-col">
        <span className="text-5xl mb-4">{icon}</span>
        <h3 className="text-white text-[20px] font-bold text-center">{title}</h3>
        <p className="mt-3 text-secondary text-[13px] text-center leading-[22px]">
          {description}
        </p>
      </div>
    </motion.div>
  </Tilt>
);

const About = () => {
  return (
    <>
      <motion.div variants={textVariant()}>
        <p className="sm:text-[18px] text-[14px] text-secondary uppercase tracking-wider">
          Introduction
        </p>
        <h2 className="text-white font-black md:text-[60px] sm:text-[50px] xs:text-[40px] text-[30px]">
          Overview.
        </h2>
      </motion.div>

      <motion.p
        variants={fadeIn("", "", 0.1, 1)}
        className="mt-4 text-secondary text-[17px] max-w-3xl leading-[30px]"
      >
        AI/ML Engineer with 10+ years of experience designing and delivering
        end-to-end AI solutions, specializing in agentic AI, LLMs, RAG, and
        multi-agent systems. Experienced in solution architecture, agent
        orchestration, prompt engineering, retrieval pipelines, model evaluation,
        and responsible AI practices. Skilled at translating complex business use
        cases into scalable, AI-driven automation.
      </motion.p>

      <div className="mt-20 flex flex-wrap gap-10 justify-center">
        {aboutCards.map((card, index) => (
          <ServiceCard key={card.title} index={index} {...card} />
        ))}
      </div>
    </>
  );
};

export default SectionWrapper(About, "about");
