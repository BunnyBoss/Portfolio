import { motion } from "framer-motion";
import { CoreCanvas } from "./canvas";
import { slideIn, textVariant } from "../utils/motion";
import { contactInfo } from "../constants";
import SectionWrapper from "../hoc/SectionWrapper";

const Contact = () => {
  return (
    <>
      <motion.div variants={textVariant()}>
        <p className="sm:text-[18px] text-[14px] text-secondary uppercase tracking-wider">
          Get in touch
        </p>
        <h2 className="font-heading text-white font-black md:text-[60px] sm:text-[50px] xs:text-[40px] text-[30px]">
          Contact.
        </h2>
      </motion.div>

      <div className="xl:mt-12 flex xl:flex-row flex-col-reverse gap-10 overflow-hidden">
        <motion.div
          variants={slideIn("left", "tween", 0.2, 1)}
          className="flex-[0.75] bg-black-100 p-8 rounded-2xl border border-white/10 hover:shadow-[0_0_30px_rgba(168,196,212,0.1)] transition-shadow duration-300"
        >
          <p className="text-secondary text-[16px] leading-[28px] mb-8">
            I'm always open to discussing Agentic AI, Multi-Agent Systems, RAG architecture, and ML in healthcare. Let's connect!
          </p>
          <div className="flex flex-col gap-6">
            <ContactItem emoji="✉️" label="Email" value={contactInfo.email} href={`mailto:${contactInfo.email}`} />
            <ContactItem emoji="📱" label="Phone" value={contactInfo.phone} href={`tel:${contactInfo.phone.replace(/\s/g, "")}`} />
            <ContactItem emoji="💼" label="LinkedIn" value="linkedin.com/in/poornachandra-g" href={contactInfo.linkedin} />
            <ContactItem emoji="🧬" label="ORCID" value="0009-0009-1610-1205" href={contactInfo.orcid} />
            <ContactItem emoji="📍" label="Location" value={contactInfo.location} />
          </div>
          <a href={`mailto:${contactInfo.email}`}
            className="mt-8 inline-block bg-accent-secondary hover:bg-accent-secondary/80 text-primary font-bold py-3 px-8 rounded-xl transition-all hover:shadow-lg hover:shadow-accent-secondary/25">
            Send Email →
          </a>
        </motion.div>

        <motion.div variants={slideIn("right", "tween", 0.2, 1)} className="xl:flex-1 xl:h-auto md:h-[550px] h-[350px]">
          {/* Space intentionally left blank for the MoonOverlay to dock into */}
        </motion.div>
      </div>
    </>
  );
};

const ContactItem = ({ emoji, label, value, href }) => (
  <div className="flex items-center gap-4 group">
    <span className="text-2xl">{emoji}</span>
    <div>
      <p className="text-secondary text-[12px] uppercase tracking-wider">{label}</p>
      {href ? (
        <a href={href} target="_blank" rel="noopener noreferrer"
          className="text-white text-[15px] hover:text-accent transition-colors">{value}</a>
      ) : (
        <p className="text-white text-[15px]">{value}</p>
      )}
    </div>
  </div>
);

export default SectionWrapper(Contact, "contact");
