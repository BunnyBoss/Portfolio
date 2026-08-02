import Tilt from "react-parallax-tilt";
import { motion } from "framer-motion";
import { projects } from "../constants";
import { fadeIn, textVariant } from "../utils/motion";
import SectionWrapper from "../hoc/SectionWrapper";

const ProjectCard = ({ index, name, description, tags, icon }) => (
  <motion.div variants={fadeIn("up", "spring", index * 0.5, 0.75)}>
    <Tilt
      tiltMaxAngleX={12}
      tiltMaxAngleY={12}
      scale={1.02}
      transitionSpeed={450}
      glareEnable={true}
      glareMaxOpacity={0.15}
      glarePosition="all"
      glareBorderRadius="16px"
      className="sm:w-[360px] w-full"
    >
      <div
        className="p-[1px] rounded-2xl shadow-card hover:shadow-[0_0_20px_rgba(168,196,212,0.2)] transition-shadow duration-300"
        style={{
          background:
            "linear-gradient(135deg, rgba(168,196,212,0.3), rgba(15,19,24,1))",
        }}
      >
        <div className="bg-tertiary rounded-2xl p-5 min-h-[320px] flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center mb-4">
              <span className="text-4xl">{icon}</span>
            </div>
            <h3 className="text-white font-bold text-[22px]">{name}</h3>
            <p className="mt-2 text-secondary text-[14px] leading-[22px]">
              {description}
            </p>
          </div>
          <div className="mt-4 flex flex-wrap gap-2">
            {tags.map((tag) => (
              <p
                key={`${name}-${tag.name}`}
                className={`text-[13px] ${tag.color}`}
              >
                #{tag.name}
              </p>
            ))}
          </div>
        </div>
      </div>
    </Tilt>
  </motion.div>
);

const Works = () => {
  return (
    <>
      <motion.div variants={textVariant()}>
        <p className="sm:text-[18px] text-[14px] text-secondary uppercase tracking-wider">
          My work
        </p>
        <h2 className="font-heading text-white font-black md:text-[60px] sm:text-[50px] xs:text-[40px] text-[30px]">
          Projects.
        </h2>
      </motion.div>

      <motion.p
        variants={fadeIn("", "", 0.1, 1)}
        className="mt-3 text-secondary text-[17px] max-w-3xl leading-[30px]"
      >
        These projects showcase my hands-on experience with agentic AI,
        multi-agent systems, RAG pipelines, and enterprise GenAI solutions.
      </motion.p>

      <div className="mt-20 flex flex-wrap gap-7 justify-center">
        {projects.map((project, index) => (
          <ProjectCard key={`project-${index}`} index={index} {...project} />
        ))}
      </div>
    </>
  );
};

export default SectionWrapper(Works, "works");
