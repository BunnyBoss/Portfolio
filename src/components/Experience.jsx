import React, { useRef } from "react";
import {
  VerticalTimeline,
  VerticalTimelineElement,
} from "react-vertical-timeline-component";
import { motion, useScroll, useTransform, useInView } from "framer-motion";
import "react-vertical-timeline-component/style.min.css";
import { experiences } from "../constants";
import { textVariant } from "../utils/motion";
import SectionWrapper from "../hoc/SectionWrapper";

const ExperienceCard = ({ experience }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { margin: "0px 0px -50% 0px" });

  return (
    <VerticalTimelineElement
      contentStyle={{
        background: "#111111",
        color: "#fff",
        borderBottom: "3px solid #00e5ff",
        border: "1px solid rgba(255, 255, 255, 0.1)",
      }}
      contentArrowStyle={{ borderRight: "7px solid #111111" }}
      date={experience.date}
      dateClassName="text-secondary"
      iconStyle={{ 
        background: experience.iconBg, 
        fontSize: "1.5rem",
        boxShadow: isInView 
          ? "0 0 0 4px #00e5ff, inset 0 2px 0 rgba(0,0,0,.08), 0 0 30px 15px rgba(0, 229, 255, 1)" 
          : "0 0 0 4px #111111, inset 0 2px 0 rgba(0,0,0,.08)",
        transition: "all 0.4s ease-in-out"
      }}
      icon={
        <div
          ref={ref}
          className="flex justify-center items-center w-full h-full text-2xl"
          style={{ 
            filter: isInView ? "drop-shadow(0 0 15px rgba(0, 229, 255, 1)) drop-shadow(0 0 30px rgba(0, 229, 255, 0.8)) grayscale(0%) opacity(100%)" : "grayscale(100%) opacity(40%)",
            transform: isInView ? "scale(1)" : "scale(0.8)",
            transition: "all 0.4s ease-in-out"
          }}
        >
          {experience.icon}
        </div>
      }
    >
    <div>
      <h3 className="text-white text-[22px] font-bold">{experience.title}</h3>
      <p className="text-accent text-[16px] font-semibold" style={{ margin: 0 }}>
        {experience.company_name}
      </p>
    </div>

    <ul className="mt-5 list-disc ml-5 space-y-2">
      {experience.points.map((point, index) => (
        <li
          key={`experience-point-${index}`}
          className="text-white-100 text-[14px] pl-1 tracking-wider leading-[22px]"
        >
          {point}
        </li>
      ))}
    </ul>
    </VerticalTimelineElement>
  );
};

const Experience = () => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start center", "end center"],
  });

  return (
    <>
      <motion.div variants={textVariant()}>
        <p className="sm:text-[18px] text-[14px] text-secondary uppercase tracking-wider">
          What I have done so far
        </p>
        <h2 className="text-white font-black md:text-[60px] sm:text-[50px] xs:text-[40px] text-[30px]">
          Work Experience.
        </h2>
      </motion.div>

      <div className="mt-20 flex flex-col relative" ref={ref}>
        {/* Glowing Scroll Line Body */}
        <motion.div 
           className="absolute left-[18px] md:left-1/2 top-0 h-full w-[4px] md:-ml-[2px] bg-accent z-0"
           style={{ 
             scaleY: scrollYProgress,
             transformOrigin: "top",
             background: "linear-gradient(to bottom, transparent, #00e5ff)",
             boxShadow: "0 0 20px 5px rgba(0, 229, 255, 0.8), 0 0 40px 10px rgba(0, 229, 255, 0.5)"
           }}
        />
        {/* Glowing Scroll Line Head */}
        <motion.div 
           className="absolute left-[18px] md:left-1/2 w-[10px] h-[30px] rounded-full bg-white md:-ml-[5px] -ml-[3px] z-0"
           style={{ 
             top: useTransform(scrollYProgress, [0, 1], ["0%", "100%"]),
             marginTop: "-30px", // Offset so the tip aligns perfectly
             boxShadow: "0 20px 50px 25px rgba(0, 229, 255, 1), 0 10px 20px 10px rgba(255, 255, 255, 1), 0 0 20px 10px #00e5ff"
           }}
        />
        <VerticalTimeline lineColor="rgba(255,255,255,0.1)">
          {experiences.map((experience, index) => (
            <ExperienceCard key={`experience-${index}`} experience={experience} />
          ))}
        </VerticalTimeline>
      </div>
    </>
  );
};

export default SectionWrapper(Experience, "experience");
